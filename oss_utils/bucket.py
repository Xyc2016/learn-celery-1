from secrets import my_key, my_secret , endpoint, bucket_name
import oss2

auth = oss2.Auth(my_key, my_secret)
learn_oss_bucket = oss2.Bucket(auth, endpoint, bucket_name)

