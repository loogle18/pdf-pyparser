import os, tarfile
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

REPORTS_ARCHIVE_PATH = '/samples/NYSE_ATO_REPORTS.tar.gz'
	
def main():
	current_path = os.getcwd()
	archive_path = os.getcwd() + REPORTS_ARCHIVE_PATH
	opened_tar = tarfile.open(archive_path, 'r:gz')
	for member in opened_tar.getmembers():
		file = opened_tar.extractfile(member)
		if file is not None:
			rsrcmgr = PDFResourceManager()
			retstr = StringIO()
			laparams = LAParams()
			device = TextConverter(rsrcmgr, retstr, laparams=laparams)
			content = retstr.getvalue()
			process_pdf(rsrcmgr, device, file)
			file.close()
			device.close()
			retstr.close()
			
			new_file_path = '{0}/{1}.txt'.format(current_path, member.name)
			with open(new_file_path, 'w') as output:
				output.write(content)

if __name__ == '__main__':
	main()