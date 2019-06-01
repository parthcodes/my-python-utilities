"""
https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python

read yaml data from configuration.yml in a object named config.
"""

import yaml


# Read Yaml file.

selected_region = "us-west-2"

with open('configuration.yml','r') as datastream:
    configs = yaml.safe_load(datastream)

for region in configs:
    if (region == selected_region):
        proxy = configs[region]['proxy']
        proxy_port = configs[region]['proxy-port']
        subnets = configs[region]['subnets']
        spark_params = configs[region]['sprak-params']
        security_groups = configs[region]['security-groups']

        #String params
        print("Proxy :" + proxy)
        print("Proxy Port :" + str(proxy_port))

        #List params - convert to string
        print("Subnets : "+ str(subnets))
        print("Security groups :" + str(security_groups))

        # Dict param - convert to string.
        print("Spark params: "+ str(spark_params))