from setuptools import setup

setup(
    name='test_packaging',
    version='0.1.0',
    package_data={"test_packaging": ["py.typed"]},
    install_requires=[
        'PyPDF2',
        'pdfplumber',
    ],
)
