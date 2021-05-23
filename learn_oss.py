import oss2
from oss_utils.bucket import learn_oss_bucket, my_secret, my_key, endpoint, bucket_name
authv2 = oss2.AuthV2(my_key, my_secret)

bucketv2 = oss2.Bucket(authv2, endpoint, bucket_name)

it = oss2.ObjectIteratorV2(bucketv2)
for o in it:
    if o.size < 1024 * 1024:
        filename = o.key
        result = bucketv2.get_object(filename)
        print(result.read())
