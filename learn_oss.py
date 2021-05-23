import oss2
from oss_utils.bucket import learn_oss_bucket, my_secret, my_key, endpoint, bucket_name
authv2 = oss2.AuthV2(my_key, my_secret)

bucketv2 = oss2.Bucket(authv2, endpoint, bucket_name)
bucketv2.put_object("05232055.txt", b"abcdef05232055")
it = oss2.ObjectIteratorV2(bucketv2)
non_archived_small_files = []
for o in it:
    
    if o.size < 1024 * 1024 and o.storage_class == "Standard":
        
        filename = o.key
        non_archived_small_files.append(filename)
        result = bucketv2.get_object(filename)
        print(result.read())

