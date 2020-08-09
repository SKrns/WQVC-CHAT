import py_eureka_client.eureka_client as eureka

registry_client, discovery_client = eureka.init(eureka_server="http://192.168.219.167:8761/eureka/",
                                                app_name="chat_server",
                                                instance_port=8081)