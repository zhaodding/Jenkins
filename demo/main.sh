#!/bin/bash


function getJsonValuesByAwk() {
    awk -v json="$1" -v key="$2" -v defaultValue="$3" 'BEGIN{
        foundKeyCount = 0
        while (length(json) > 0) {
            # pos = index(json, "\""key"\""); ## 这行更快一些，但是如果有value是字符串，且刚好与要查找的key相同，会被误认为是key而导致值获取错误
            pos = match(json, "\""key"\"[ \\t]*?:[ \\t]*");
            if (pos == 0) {if (foundKeyCount == 0) {print defaultValue;} exit 0;}

            ++foundKeyCount;
            start = 0; stop = 0; layer = 0;
            for (i = pos + length(key) + 1; i <= length(json); ++i) {
                lastChar = substr(json, i - 1, 1)
                currChar = substr(json, i, 1)

                if (start <= 0) {
                    if (lastChar == ":") {
                        start = currChar == " " ? i + 1: i;
                        if (currChar == "{" || currChar == "[") {
                            layer = 1;
                        }
                    }
                } else {
                    if (currChar == "{" || currChar == "[") {
                        ++layer;
                    }
                    if (currChar == "}" || currChar == "]") {
                        --layer;
                    }
                    if ((currChar == "," || currChar == "}" || currChar == "]") && layer <= 0) {
                        stop = currChar == "," ? i : i + 1 + layer;
                        break;
                    }
                }
            }

            if (start <= 0 || stop <= 0 || start > length(json) || stop > length(json) || start >= stop) {
                if (foundKeyCount == 0) {print defaultValue;} exit 0;
            } else {
                print substr(json, start, stop - start);
            }

            json = substr(json, stop + 1, length(json) - stop)
        }
    }'
}


json=${kubectl -n ke-dev get deployment centos-test -o json}

name=getJsonValuesByAwk "$json" "name" "defaultValue"|head -n 1
namespace=getJsonValuesByAwk "$json" "namespace" "defaultValue"|head -n 1
memeory=getJsonValuesByAwk "$json" "memory" "defaultValue"|head -n 1

key1value=name+","+namespace+","+memeory
#必须先声明
declare -A dic
dic=([key1]="name,nameshpace,memeory" [key2]="value2" [key3]="value3")

#打印指定key的value
echo ${dic["key1"]}

#echo ${dic["key1"]} |awk -F, '{print $1}'
name=${dic["key1"]} |awk -F, '{print $1}'
namespace=${dic["key1"]} |awk -F, '{print $2}'
memeory=${dic["key1"]} |awk -F, '{print $3}'



 #expr index $var "--server.port
string="#!/bin/sh cp agent.config /usr/local/skywalking-agent/config/agent.config exec java -javaagent:/usr/local/skywalking-agent/skywalking-agent.jar -Dskywalking.agent.service_name=nobo-pcp-oc-service-uat -Dskywalking.collector.backend_service=10.42.6.208:33001 -Djava.security.egd=file:/dev/./urandom -Duser.timezone=GMT+08 -Xms1024m -Xmx1024m -jar /opt/app.jar --server.port=8080 --spring.profiles.active=prd --logging.config=/opt/logback-spring.xml --spring.config.location=application-prd.yml,classpath:BOOT-INF/classes/application.yml"
array=(${string//,/ })

for var in ${array[@]}
do
   if [[ $var =~ "--logging.config=" ]]
then
    echo "包含"
    echo $var
else
    echo "不包含"
fi
done











