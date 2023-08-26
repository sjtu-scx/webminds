# import requests
# from lxml import html

# # 发送请求并获取网页内容
# url = "https://www.chyxx.com/research/202103/935022.html?bd_vid=8237899329342221593"  # 将此处替换为您想要提取XPath的网页链接
# response = requests.get(url)
# html_content = response.content

# # 将网页内容解析为HTML树
# tree = html.fromstring(html_content)

# # 辅助函数：检查节点是否为叶子节点
# def is_leaf(element):
#     return len(element) == 0

# # 获取前10个叶子节点的XPath表达式
# leaf_xpaths = []
# for element in tree.iter():
#     if is_leaf(element):
#         xpath = tree.getroottree().getpath(element)
#         leaf_xpaths.append(xpath)
#         if len(leaf_xpaths) == 50:
#             break

# # 打印前10个叶子节点的XPath
# for i, xpath in enumerate(leaf_xpaths):
#     print(f"Leaf Node XPath {i + 1}: {xpath}")

import requests
from lxml import html

# 发送请求并获取网页内容
url = "https://www.chyxx.com/research/202103/935022.html?bd_vid=8237899329342221593"  # 将此处替换为您想要提取内容的网页链接
response = requests.get(url)
html_content = response.content

# 将网页内容解析为HTML树
tree = html.fromstring(html_content)

# 辅助函数：检查节点是否为叶子节点
def is_leaf(element):
    return len(element) == 0

# 获取前10个叶子节点的内容和XPath表达式
leaf_nodes = []
cnt = 0
for element in tree.iter():
    if not isinstance(element, html.HtmlComment) and is_leaf(element):
        xpath = tree.getroottree().getpath(element)
        content = element.text_content().strip()
        leaf_nodes.append({"xpath": xpath, "content": content})
        cnt += 1
        # if len(leaf_nodes) == 200:
        #     break
print(cnt)
# 打印前10个叶子节点的内容和XPath
# for i, node in enumerate(leaf_nodes):
#     print(f"Leaf Node {i + 1} XPath: {node['xpath']}")
#     print(f"Content: {node['content']}")
#     print("=" * 30)
