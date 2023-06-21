# import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By


# class Test_Pytest:
#     def test_sum_005(self):
#         a = 7
#         b = 4
#         sum = a + b
#         # print(sum)
#         if sum == 11:
#             assert True
#         else:
#             assert False

#     def test_Credence_006(self):
#         driver = webdriver.Chrome()
#         driver.get("https://credence.in/")
#         time.sleep(2)
#         driver.find_element(
#             By.XPATH, "//img[@src='/website/images/enquiry.png']"
#         ).click()
#         l = len(
#             driver.find_elements(
#                 By.XPATH,
#                 "//div[@class='quickfinder-description gem-text-output']//p//a",
#             )
#         )
#         # print(l)
#         Contact_Number_List = []
#         for r in range(1, l + 1):
#             Contact_Number = driver.find_element(
#                 By.XPATH,
#                 "//div[@class='quickfinder-description gem-text-output']//p//a["
#                 + str(r)
#                 + "]",
#             ).text
#             # print(Contact_Number)
#             Contact_Number_List.append(Contact_Number)
#         # print(Contact_Number_List)
#         mb = "+91 9579064658"
#         if mb in Contact_Number_List:
#             print(Contact_Number_List.index(mb))
#             assert True
#         else:
#             assert False

# import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By


# class Test_Pytest:
#     def test_sum_005(self):
#         a = 7
#         b = 4
#         sum = a + b
#         # print(sum)
#         if sum == 11:
#             assert True
#         else:
#             assert False

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# class Test_pytest:
#     def test_sum_006(self):
#         a = 6
#         b = 8
#         sum = a + b
#         if sum == 14:
#             assert True
#         else:
#             assert False

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_pytest:
    def test_Credence_Url_010(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("You are at Right place")
        else:
            print("You are at Wrong place")
