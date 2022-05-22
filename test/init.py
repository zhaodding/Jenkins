# @Organization: 上海敏桥信息科技有限公司
# @Author      : Kevin
# @Time        : 2022/5/18 9:51
# @Function    :

from kubernetes.client import BatchV1Api
from kubernetes.config import load_kube_config

load_kube_config()
batch = BatchV1Api()