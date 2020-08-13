
import pystache
#渲染模板文件，返回渲染后的内容
class Template:

    @classmethod
    def render(cls, path, dict):
        try:
            render = pystache.Renderer(escape=lambda u: u)
            with open(path) as f:
                content = f.read()
                parsed = pystache.parse(content)
                result = render.render(parsed, dict)
                return result
        except Exception as e:
            raise e
