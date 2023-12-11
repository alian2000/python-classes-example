from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
namespace = input ("what namespace? ")

#def get_pods():
v1 = client.CoreV1Api()
svc_list = v1.list_namespaced_service(namespace)
for svc in svc_list.items:
    print("%s\t%s\t%s" % (svc.metadata.name,
        svc.status.phase,
        svc.status.pod_ip))