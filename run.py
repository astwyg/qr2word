### refer:
# https://docxtpl.readthedocs.io/en/latest/
# https://pypi.org/project/qrcode/

import qrcode
from docxtpl import DocxTemplate, InlineImage
from io import BytesIO

if __name__ == "__main__":
    # make qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data("https://baidu.com")
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    file_like = BytesIO()
    img.save(file_like)

    # create word with NO file on disk.
    doc = DocxTemplate("template.docx")
    context = {
        'word': "baidu.com",
        'img': InlineImage(doc, file_like)
    }
    doc.render(context)
    doc.save("out.docx")

