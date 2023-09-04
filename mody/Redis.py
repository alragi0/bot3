from redis import StrictRedis

# تعيين المعلمات الخاصة بالاتصال
host = "containers-us-west-177.railway.app"  # عنوان خادم Redis
port = 7718  # المنفذ الذي ترغب في استخدامه
password = "E4Zm1vpbzc0R3CXM31Hh"  # كلمة المرور إذا كانت مطلوبة

# إنشاء اتصال Redis
db = StrictRedis(host=host, port=port, password=password, decode_responses=True)

# الآن يمكنك استخدام الاتصال db للقيام بالعمليات على خادم Redis بالمنفذ المحدد
