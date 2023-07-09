import os,sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),".."))) # To create cache and to collapse the folders
from Payment import payment_details
def course_aaa():
    print("this is my course file")

payment_details.payment_aaa() # Calling the payment_aaa functions from the module "payment_details"