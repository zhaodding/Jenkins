# @Organization: 上海敏桥信息科技有限公司
# @Author      : Kevin
# @Time        : 2022/5/18 9:57
# @Function    :

from kubernetes import client, config
config.kube_config.load_kube_config(config_file="kubeconfig.yaml")


class Kubernetes:
  def __init__(self):
    self.Connect = client.CoreV1Api()

  def ListNameSpace(self):
    data = []
    for ns in self.Connect.list_namespace().items:
      data.append(ns.metadata.name)
    return data

  def CreateNameSpace(self,name):
    body = client.V1Namespace()
    body.metadata = client.V1ObjectMeta(name=name)
    return self.Connect.create_namespace(body=body)

  def ListPod(self, namespace):
    res = self.Connect.list_pod_for_all_namespaces(watch=False)
    for i in res.items:
      if i.metadata.namespace == namespace:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

  def ListService(self, namespace):
    res = self.Connect.list_service_for_all_namespaces(watch=False)
    for i in res.items:
      if i.metadata.namespace == namespace:
        print("%s \t%s \t%s \t%s \n" % (i.metadata.namespace, i.metadata.name, i.spec.cluster_ip, i.spec.ports))

  def pod_info(self, name, namespace):
    res = self.Connect.read_namespaced_pod(name, namespace)
    # print(res.spec)
    # print(res.status)
    # print(res.spec.containers[0].image)
    # print(res.spec.containers[0].ports[0].container_port)
    # print(res.spec.node_name)
    print('pod_ip: %s\ncontainer_port: %s\nnode_name: %s\nhost_ip: %s' %(res.status.pod_ip, res.spec.containers[0].ports[0].container_port, res.spec.node_name, res.status.host_ip))

k = Kubernetes()
k.pod_info('my-nginx-demo-0', 'default')
# print(k.ListNameSpace())
# k.ListPod('default')
# k.ListService('default')
