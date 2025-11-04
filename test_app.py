import requests
import csv
from datetime import datetime
import time

REAL_TEST_CASE_1 = "KT Rolster and T1 will face off in an all-LCK grand final at the 2025 League of Legends World Championship after securing decisive victories in Shanghai over the past week. Riot Games said the quarterfinals and semifinals, held Oct. 28–Nov. 2 at Mercedes-Benz Arena, ended with both Korean squads advancing to the title match. The best-of-five final is scheduled for Nov. 9 at Chengdu’s Dong’an Lake Sports Park Multi-Purpose Gymnasium, marking the first Worlds final between LCK teams since 2022. KT Rolster’s run to the championship stage marks the organization’s first Worlds final since entering League of Legends in 2012. T1, meanwhile, is seeking a historic third consecutive championship and a fourth straight finals appearance."
REAL_TEST_CASE_2 = """US President Donald Trump's administration has said it will provide reduced food aid to more than 42 million Americans, as the government shutdown this week heads towards becoming the longest ever with no resolution in sight.

The US Department of Agriculture (USDA) said in a court filing that Americans who receive food assistance will get half their normal monthly allotment, after the government dipped into emergency funding."""

FAKE_TEST_CASE_1 = "Hello, My name is Rayan."
FAKE_TEST_CASE_2 = "Hello, I am the best Coder in the World."

# real_response_1 = requests.post(
#     "http://server-sentiment-env.eba-vqgsakps.us-east-2.elasticbeanstalk.com/predict",
#     json={"message": REAL_TEST_CASE_1}
# )

# real_response_2 = requests.post(
#     "http://server-sentiment-env.eba-vqgsakps.us-east-2.elasticbeanstalk.com/predict",
#     json={"message": REAL_TEST_CASE_2}
# )

# fake_response_1 = requests.post(
#     "http://server-sentiment-env.eba-vqgsakps.us-east-2.elasticbeanstalk.com/predict",
#     json={"message": FAKE_TEST_CASE_1}
# )

# fake_response_2 = requests.post(
#     "http://server-sentiment-env.eba-vqgsakps.us-east-2.elasticbeanstalk.com/predict",
#     json={"message": FAKE_TEST_CASE_2}
# )

rows = [["Test Case", "Timestamp", "JSON Response"]]
test1_rows = rows.copy()
test2_rows = rows.copy()
test3_rows = rows.copy()
test4_rows = rows.copy()

# print(real_response_1.json())
# print(real_response_2.json())
# print(fake_response_1.json())
# print(fake_response_2.json())

for i in range(100):
    real_response_1 = requests.post(
        "http://server-sentiment-env.eba-vqgsakps.us-east-2.elasticbeanstalk.com/predict",
        json={"message": REAL_TEST_CASE_1}
    )
    row = ["REAL_TEST_CASE_1", str(time.time()), real_response_1.json()['label']]
    test1_rows.append(row)
    rows.append(row)

for i in range(100):
    real_response_2 = requests.post(
        "http://server-sentiment-env.eba-vqgsakps.us-east-2.elasticbeanstalk.com/predict",
        json={"message": REAL_TEST_CASE_2}
    )
    row = ["REAL_TEST_CASE_2", str(time.time()), real_response_2.json()['label']]
    test2_rows.append(row)
    rows.append(row)

for i in range(100):
    fake_response_1 = requests.post(
        "http://server-sentiment-env.eba-vqgsakps.us-east-2.elasticbeanstalk.com/predict",
        json={"message": FAKE_TEST_CASE_1}
    )
    row = ["FAKE_TEST_CASE_1", str(time.time()), fake_response_1.json()['label']]
    test3_rows.append(row)
    rows.append(row)

for i in range(100):
    fake_response_2 = requests.post(
        "http://server-sentiment-env.eba-vqgsakps.us-east-2.elasticbeanstalk.com/predict",
        json={"message": FAKE_TEST_CASE_2}
    )
    row = ["FAKE_TEST_CASE_2", str(time.time()), fake_response_2.json()['label']]
    test4_rows.append(row)
    rows.append(row)

with open("test1.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(test1_rows)

with open("test2.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(test2_rows)

with open("test3.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(test3_rows)

with open("test4.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(test4_rows)

with open("test.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)