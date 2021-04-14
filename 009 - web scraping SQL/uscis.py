import time
import asyncio
import concurrent.futures
import requests
import matplotlib.pyplot as plt

RECEIPT_NUMBER_BASE = "MCT2052"
RANGE_START = 595222
RANGE_END = 595822
CASE_TYPE = 'I-539'
CONCURRENCY_LEVEL = 11


def check_status(receipt_num):
    #print(receipt_num)
    pload = {"appReceiptNum": receipt_num, "initCaseSearch":"CHECK STATUS"}
    r = requests.post('https://egov.uscis.gov/casestatus/mycasestatus.do', data=pload)
    if (r.status_code != 200):
        print("Error with {0}, code {1}".format(receipt_num, r.status_code))
        return None
    
    response = r.text.split("\n")
    
    if CASE_TYPE in response[735]:
        return (receipt_num, response[721].strip())
    else:
        return None


def save_plot(status_list):
    x, y = zip(*status_list)
    plt.scatter(x, y)
    plt.show()
    plt.savefig('UscisStats.png', bbox_inches='tight')

status_list = []

async def main():
    num_digits = len(str(RANGE_END))

    loop = asyncio.get_event_loop()
    batches = int((RANGE_END - RANGE_START) / CONCURRENCY_LEVEL + 1)
    print("Running total {} batches".format(batches))
    start = time.time()
    for i in range(batches):
        if i % 10 == 0:
            seconds = time.time() - start
            print(" - processing batch No.{0}, the job has took {1:.2f} seconds.".format(i, seconds))
            print(" - Has found I-765: {}".format(len(status_list)))
        batch_start = RANGE_START + CONCURRENCY_LEVEL * i
        with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENCY_LEVEL) as executor:
            loop = asyncio.get_event_loop()
            futures = [
                loop.run_in_executor(
                    executor,
                    check_status,
                    RECEIPT_NUMBER_BASE + str(batch_start+x).zfill(num_digits)
                )
                for x in range(CONCURRENCY_LEVEL)
            ]
            for t in await asyncio.gather(*futures):
                if t is not None:
                    status_list.append(t)
            
                    
    print('{0} takes {1:.2f}% in the range.'.format(CASE_TYPE, 100*len(status_list)/(batches*CONCURRENCY_LEVEL)))

    save_plot(status_list)


loop = asyncio.get_event_loop()
loop.create_task(main())