def is_bulk(request):
    url = request.path[1:]
    if 'bulk' in url:
        return True
    else:
        return False