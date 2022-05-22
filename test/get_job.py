# @Organization: 上海敏桥信息科技有限公司
# @Author      : Kevin
# @Time        : 2022/5/18 9:49
# @Function    :


from typing import List

from kubernetes.client import CoreV1Api, V1Pod


def get_pods_by(job_name: str) -> List[V1Pod]:
    core = CoreV1Api()
    pods = core.list_namespaced_pod(
        namespace='default',
        label_selector=f'job-name={job_name}',
        limit=1,
    )
    return pods.items