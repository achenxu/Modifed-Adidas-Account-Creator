import datetime
import time
from random import randint
import requests
from bs4 import BeautifulSoup

def accountCreated(region, response):
    hms = time.strftime("%H:%M:%S")
    hmsString = "[" + hms + "] "

    if (region == "US") or (region == "us"):
        try:
            return False if BeautifulSoup(response.text, "html.parser").find('input',
                                                                             {'id': 'resumeURL'}).get('value') == \
                            'https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MyAccount-CreateOrLogin' \
                else True
        except:
            return True

def generateUS(region):
    hms = str(datetime.timedelta(seconds=666))
    hmsString = "[" + hms + "] "

    print("Adidas Account Generator by Gleb-io\n" + "Based off Adidas-Account-Gen by Simmycop & Doprdele\n")
    fnameString = input(hmsString + "Enter your first name for the accounts: ")
    lnameString = input(hmsString + "Enter your last name for the accounts: ")
    emailString = input(hmsString + "Enter prefix of your email: ")
    passString = input(hmsString + "Enter a desired password for the account: ")
    amountString = input(hmsString + "How many accounts do you want made: ")
    amountString = int(amountString)

    i = 0

    while (i < amountString):
        email = emailString + '.' + str(randint(0, 999999)) + '@gmail.com'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'en-US,en;q=0.8',
            'Upgrade-Insecure-Requests': '1'
        }

        s = requests.Session()
        s.headers.update(headers)

        r = s.get('https://cp.adidas.com/web/eCom/en_US/loadcreateaccount')
        csrftoken = BeautifulSoup(r.text, "html.parser").find('input', {'name':'CSRFToken'}).get('value')

        s.headers.update({
            'Origin': 'https://cp.adidas.com',
            'Referer': 'https://cp.adidas.com/web/eCom/en_US/loadcreateaccount',
        })

        r = s.post('https://cp.adidas.com/web/eCom/en_US/accountcreate',
                   data={
                       'firstName': fnameString,
                       'lastName': lnameString,
                       'minAgeCheck': 'true',
                       '_minAgeCheck': 'on',
                       'email': email,
                       'password': passString,
                       'confirmPassword': passString,
                       '_amf': 'on',
                       'terms': 'true',
                       '_terms': 'on',
                       'metaAttrs[pageLoadedEarlier]': 'true',
                       'app': 'eCom',
                       'locale': 'en_US',
                       'domain': '',
                       'consentData1': 'Sign me up for adidas emails, featuring exclusive offers, featuring latest product info, news about upcoming events, and more. See our <a target="_blank" href="https://www.adidas.com/us/help-topics-privacy_policy.html">Policy Policy</a> for details.',
                       'consentData2': '',
                       'consentData3': '',
                       'CSRFToken': csrftoken
                   })

        if (accountCreated(region, r) == False):
            print(hmsString + "Account EXISTS : Username = {0}, Password = {1}".format(emailString, passString))

        if (accountCreated(region, r) == True):
            print(hmsString + "Created Account with prefix = {0}, Password = {1}".format(emailString, passString))
            with open('accounts' + '.txt', 'a') as f:
                f.write("Email Address: " + email + ' - Password: ' + passString + '\n')
                f.close()

        i = i + 1

        time.sleep(5)


generateUS("us")
