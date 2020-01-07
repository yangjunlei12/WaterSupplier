class JsonFactory:
    def makeJson(self, obj, *args):
        '''
        实际上返回的是dict类型
        '''
        if args:
            json = {}
            for name in args:
                if hasattr(obj, name):
                    json[name] = getattr(obj, name)
                else:
                    return None
            return json
        return None

    def makeJsonList(self, objs, pages, *args):
        json_list = []
        if pages == 0:
            if objs.count() > 10:
                for obj in objs.order_by('-id')[:10]:
                    json = self.makeJson(obj, *args)
                    if json:
                        json_list.append(json)
            else:
                for obj in objs.order_by('-id'):
                    json = self.makeJson(obj, *args)
                    if json:
                        json_list.append(json)
        else:
            if objs.count() > pages:
                for obj in objs.order_by('-id')[:pages]:
                    json = self.makeJson(obj, *args)
                    if json:
                        json_list.append(json)
            else:
                for obj in objs.order_by('-id'):
                    json = self.makeJson(obj, *args)
                    if json:
                        json_list.append(json)
        return json_list