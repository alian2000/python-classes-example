from kubernetes import client, config
config.load_kube_config()

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
node_list=v1.list_node()
for node in node_list.items:

    print(node.metadata.name,
         node.metadata.labels,
         node.metadata.annotations)
