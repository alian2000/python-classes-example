from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
namespace = input ("what namespace? ")

#def get_pods():
v1 = client.CoreV1Api()
pod_list = v1.list_namespaced_pod(namespace)
for pod in pod_list.items:
    #print("%s\t%s\t%s" % (pod.metadata.name,
                          pod.status.phase,
                          pod.status.pod_ip))

