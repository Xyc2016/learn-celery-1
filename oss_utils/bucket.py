from secrets import my_key, my_secret
import oss2

auth = oss2.Auth(my_key, my_secret)
learn_oss_bucket = oss2.Bucket(auth,"oss-cn-zhangjiakou.aliyuncs.com","xyc-learn-oss")

