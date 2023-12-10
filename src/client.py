from tasks import build_server_with_cleanup

result = build_server_with_cleanup.delay()
print("doing ...")
print(result)
