import os
import sys
import json
import time
import random
import requests
from tqdm import tqdm

# request_quora function takes in a "query" and an "after" value
def request_quora(query, first, after):

    # request quora.com/search?q=python&type=question , and get the response

    cookies = {
        'm-b': 'Kt17F42mjIu8PcBxY00RVg==',
        'm-s': 'MC_679A0Oo4q5VRwWmxXeg==',
        'm-b_lax': 'Kt17F42mjIu8PcBxY00RVg==',
        'm-b_strict': 'Kt17F42mjIu8PcBxY00RVg==',
        'm-theme': 'light',
        'm-dynamicFontSize': 'regular',
        'm-sa': '1',
        'g_state': '{"i_l":0}',
        'm-lat': 'RbMmNmNx-8q0hpIBXFlhFg==',
        'm-login': '1',
        'm-uid': '2237329375',
        '_scid': '7498e6ac-f9a2-4545-9302-f7c7246e57bc',
        '_scid_r': '7498e6ac-f9a2-4545-9302-f7c7246e57bc',
        '_fbp': 'fb.1.1692195829786.5571278',
        '_gcl_au': '1.1.1591887107.1692195830',
        '_sctr': '1%7C1692115200000',
        '_sc_cspv': 'https%3A%2F%2Ftr.snapchat.com%2Fp%3Fv%3D2',
        '__gads': 'ID=95ec9ab107cbdcd5-222a9b5083df00dd:T=1683249991:RT=1692807986:S=ALNI_MbARQ-5VwXAV2wYz0RF1iWxgYV-iw',
        '__gpi': 'UID=000009867dd12059:T=1683249991:RT=1692807986:S=ALNI_Ma9r1NXMcY-QhssjLfQaNe9hB_fcw',
        'ans_frontend-ql10n_ar': 'https%3A%2F%2Fqsc.cf2.quoracdn.net%2F-4-l10n_main-30-ar-51aae518e35b46e9.translation.json',
        'm-ql10n_ar': 'https%3A%2F%2Fqsc.cf2.quoracdn.net%2F-4-l10n_main-30-ar-d6bdd497e3820034.translation.json',
        'OptanonAlertBoxClosed': '2023-08-24T02:12:10.813Z',
        'OptanonConsent': 'isIABGlobal=false&datestamp=Thu+Aug+24+2023+10%3A12%3A11+GMT%2B0800+(China+Standard+Time)&version=6.32.0&hosts=&consentId=33248f78-58a9-497c-ae9d-29a75f9a9e95&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=CN%3BGD',
    }

    headers = {
        'authority': 'ar.quora.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6',
        'content-type': 'application/json',
        # 'cookie': 'm-b=Kt17F42mjIu8PcBxY00RVg==; m-s=MC_679A0Oo4q5VRwWmxXeg==; m-b_lax=Kt17F42mjIu8PcBxY00RVg==; m-b_strict=Kt17F42mjIu8PcBxY00RVg==; m-theme=light; m-dynamicFontSize=regular; m-sa=1; g_state={"i_l":0}; m-lat=RbMmNmNx-8q0hpIBXFlhFg==; m-login=1; m-uid=2237329375; _scid=7498e6ac-f9a2-4545-9302-f7c7246e57bc; _scid_r=7498e6ac-f9a2-4545-9302-f7c7246e57bc; _fbp=fb.1.1692195829786.5571278; _gcl_au=1.1.1591887107.1692195830; _sctr=1%7C1692115200000; _sc_cspv=https%3A%2F%2Ftr.snapchat.com%2Fp%3Fv%3D2; __gads=ID=95ec9ab107cbdcd5-222a9b5083df00dd:T=1683249991:RT=1692807986:S=ALNI_MbARQ-5VwXAV2wYz0RF1iWxgYV-iw; __gpi=UID=000009867dd12059:T=1683249991:RT=1692807986:S=ALNI_Ma9r1NXMcY-QhssjLfQaNe9hB_fcw; ans_frontend-ql10n_ar=https%3A%2F%2Fqsc.cf2.quoracdn.net%2F-4-l10n_main-30-ar-51aae518e35b46e9.translation.json; m-ql10n_ar=https%3A%2F%2Fqsc.cf2.quoracdn.net%2F-4-l10n_main-30-ar-d6bdd497e3820034.translation.json; OptanonAlertBoxClosed=2023-08-24T02:12:10.813Z; OptanonConsent=isIABGlobal=false&datestamp=Thu+Aug+24+2023+10%3A12%3A11+GMT%2B0800+(China+Standard+Time)&version=6.32.0&hosts=&consentId=33248f78-58a9-497c-ae9d-29a75f9a9e95&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=CN%3BGD',
        'origin': 'https://ar.quora.com',
        'quora-broadcast-id': 'main-w-chan54-8888-react_sriqihcubhsksbyy-JCsr',
        'quora-canary-revision': 'false',
        'quora-formkey': '4d959383ba36a015f4d5cf165938c5da',
        'quora-page-creation-time': '1692843123696381',
        'quora-revision': '532853e677500de7ed46bee92d8487254f7f7654',
        'quora-window-id': 'react_sriqihcubhsksbyy',
        'referer': 'https://ar.quora.com/search?q=%D8%B9%D8%A7%D8%A6%D9%84%D8%A9&type=question',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    params = {
        'q': 'SearchResultsListQuery',
    }

    json_data = {
        'queryName': 'SearchResultsListQuery',
        'variables': {
            'query': query,
            'disableSpellCheck': None,
            'resultType': 'question',
            'author': None,
            'time': 'all_times',
            'first': first,
            'after': after,
            'tribeId': None,
        },
        'extensions': {
            'hash': 'fda0eef0da5b7595289628f166e1c163a5fec61ae157f50a258558456c749df1',
        },
    }

    flag = True
    fail_trial = 0

    while flag:
        raw_response = requests.post(
            'https://ar.quora.com/graphql/gql_para_POST',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
        )

        try:
            response = json.loads(raw_response.text)
            question_list = []

            # with open("debug_ar.txt", "w", encoding="utf-8") as f:
            #     json.dump(response, f, ensure_ascii=False, indent=4)

            try:
                test = response['data']['searchConnection']['edges']            # if this line works, then the page is not blank
                flag = False

                for edge_idx in range(len(test)):                               # len(test) is 10 or less than 10 if at the bottom
                    raw_title = response['data']['searchConnection']['edges'][edge_idx]['node']['question']['title']
                    dict_title = json.loads(raw_title)
                    question = dict_title['sections'][0]['spans'][0]['text']
                    question_list.append(question)
                return question_list, fail_trial

            except:
                print(f"1 Blank Page at --- 'query': '{query}' | after: '{after}'")
                flag = True
                fail_trial += 1
                if fail_trial == 10:
                    flag = False
                    return [], fail_trial
        except:
            print(f"request failed at 'query': '{query}' | after: '{after}', retrying...")
            flag = True
            fail_trial += 1
            if fail_trial == 10:
                flag = False
                return [], fail_trial
        




def control(query, max_question_num):
    flag = True
    fail_trial_2 = 0

    while flag:
        query = query

        with open(f"query_{query}.txt", "r", encoding="utf-8") as check_file:
            question_num = sum(1 for line in check_file)
            # print("question_num: ", question_num)
            after = str(question_num)

        if (max_question_num - question_num) < 10:
            first = max_question_num - question_num 
        else:
            first = 10

        new_question_list, fail_trial = request_quora(query, first, after)
        time.sleep(random.randint(50, 60)/100)

        if len(new_question_list) == 0:
            print(f"2 Blank Page at --- 'query': '{query}' | after: '{after}'")
            fail_trial_2 += 1
            flag = True
        
        if fail_trial == 10 or fail_trial_2 == 10:
            with open(f"query_{query}.txt", "a", encoding="utf-8") as f:
                for question in new_question_list:
                    f.write(question + "\n")

            os.rename(f"query_{query}.txt", f"query_{query}_done_{after}.txt")
            flag = False        

        if 0 < len(new_question_list) < 10 or question_num >= max_question_num:             # stop the iteration: 1000 questions or bottom touched
            with open(f"query_{query}.txt", "a", encoding="utf-8") as f:
                for question in new_question_list:
                    f.write(question + "\n")

            os.rename(f"query_{query}.txt", f"query_{query}_done_{max_question_num}.txt")
            flag = False        

        else:                                                               # normal, 10 questions case
            with open(f"query_{query}.txt", "a", encoding="utf-8") as f:
                for question in new_question_list:
                    f.write(question + "\n")
        

def main(max_question_num, file_name):

    # Step 1: Open a file in write mode and redirect stdout to it
    # original_stdout = sys.stdout
    # with open(f'output_log_{time.time()}.txt', 'w', encoding='utf-8') as file:
    #     sys.stdout = file
        
    start_time_1 = time.time()
    print("-"*100)
    print("Crawling started...")

    with open(file_name, "r", encoding="utf-8") as f:
        query_list = [query.strip() for query in f.readlines()]
        print("All query list:", query_list)

    max_question_num = max_question_num
    all_files = os.listdir()
    processed_query_list = []

    print("-"*100)
    for query in query_list:
        for file in all_files:
            if file.startswith(f"query_{query}_done"):
                print(f"query: {query} has been processed before, skipping...")
                processed_query_list.append(query)
                break

    unprocessed_query_list = [query for query in query_list if query not in processed_query_list]
    print("-"*100)
    print(f"unprocessed_query_list now: {unprocessed_query_list}")

    # Initialize the progress bar

    count = 0
    for query in unprocessed_query_list:
        print("-"*100)
        print(f"Currently processing query: {query}")
        with open(f"query_{query}.txt", "a") as file:
            pass
        start_time_2 = time.time()
        control(query, max_question_num)
        print(f"total time consumption: {time.time()-start_time_2} seconds")
        count += 1
        if not count == len(unprocessed_query_list):
            print(f"query: {query} has been processed, moving on to the next query...")
        else:
            print(f"query: {query} has been processed")
            print("-"*100)
            print(f"All queries done! Crawling finished! Total time consumption: {time.time()-start_time_1} seconds")
    # sys.stdout = original_stdout







main(max_question_num=1000, file_name="query_list_ar_sample.txt")