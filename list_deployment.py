from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
namespace = input ("what namespace? ")

#def get_pods():
v1 = client.CoreV1Api()
deploy_list = v1.list_namespaced_deployment(namespace)
for deploy in deploy_list.items:
    print("%s\t%s\t%s" % (deploy.metadata.name,
                          deploy.status.phase,
                          deploy.status.pod_ip))