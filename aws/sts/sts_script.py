import boto3
from bson import json_util
import json
import fileinput
import os

def find_between(s, first, last):
	try:
		start = s.index(first) + len(first)
		end = s.index(last, start)
		return s[start:end]
	except ValueError:
		return ''


def find_between_r(s, first, last):
	try:
		start = s.rindex(first) + len(first)
		end = s.rindex(last, start)
		return s[start:end]
	except ValueError:
		return ''

def main():
	#client = boto3.client('sts')
	session = boto3.Session(profile_name='default')
	client	= session.client('sts')
	response = client.assume_role(
	    RoleArn='arn:aws:iam::022341759614:role/akshay-custom-role',
	    RoleSessionName='sts',
	#    Policy='string',
	#    DurationSeconds=123,
	#    ExternalId='string',
	#    SerialNumber='string',
	#    TokenCode='string'
	)
	#print(str(response).replace("u'","'").replace("'",'"'))

	#following remove n' from json reponse & make pretty json with double quotes, earlier single quote json n' was coming
	formatted_json_string=json.dumps(response,default=json_util.default)
	#print(formatted_json_string)
	parsed_json = json.loads(formatted_json_string)
	#Json Parsing
	accessKeyId = parsed_json["Credentials"]["AccessKeyId"]
	SecretAccessKey = parsed_json["Credentials"]["SecretAccessKey"]
	SessionToken = parsed_json["Credentials"]["SessionToken"]
	Expiration = str(parsed_json["Credentials"]["Expiration"]["$date"])


	print("AccessKeyId : "+accessKeyId )
	print("SecretAccessKey : "+SecretAccessKey )
	print("SessionToken : "+SessionToken)
	print("Expiration : "+ Expiration )
	#print("Expiration : "+str(parsed_json["Credentials"]["Expiration"]) )
	#print("Expiration : "+json.dumps(parsed_json["Credentials"]["Expiration"],default=json_util.default) )
	

	#update credentials file in .aws folder
	update_aws_credentials('/home/swansh/.aws/credentials',accessKeyId,SecretAccessKey,SessionToken,Expiration,'sts')


# def update_aws_credentials(file_name,accesskeyid):
# 	tempFile = open( file_name, 'r+' )
# 	for line in fileinput.input( file_name ):
# 		if "aws_access_key_i1d" in line :
# 			tempFile.write( line.replace(find_between(str(line),"aws_access_key_id = ",'\n').strip(), accesskeyid))
# 			print("found......")
# 	tempFile.close()

def update_aws_credentials(file_name,accesskeyid,secretcccesskey,sessiontoken,expiration,profile):
	filedata = None
	with open(file_name, 'r') as file :
		filedata = file.read()

	default_data=find_between(filedata,'[default]','['+profile+']')
	profile_data=find_between_r(filedata,'['+profile+']',os.linesep)+os.linesep
	# Replace the target string
	profile_data1 = profile_data.replace(find_between(profile_data,'aws_access_key_id = ',os.linesep), accesskeyid)
	profile_data2 = profile_data1.replace(find_between(profile_data1,'aws_secret_access_key = ',os.linesep), secretcccesskey)
	profile_data3 = profile_data2.replace(find_between(profile_data2,'aws_session_token = ',os.linesep), sessiontoken)
	profile_data4 = profile_data3.replace(find_between(profile_data3,'token_expiration = ',os.linesep), expiration)
	
	#print(find_between(filedata,'aws_access_key_id = ',os.linesep))
	#print(find_between_r(filedata,'['+profile+']',os.linesep))

	# os.linesep is end of line char based on operation system

	final_file_string='[default]'+default_data+'['+profile+']'+profile_data4

	# Write the file out again
	with open(file_name, 'w') as file:
		file.write(final_file_string)

if __name__ == '__main__':
	main()
