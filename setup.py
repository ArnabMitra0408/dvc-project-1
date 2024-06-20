from setuptools import setup,find_packages

with open ('README.md','r',encoding='utf-8') as f:
    long_description=f.read()

setup(
    name='src',
    version='0.0.1',
    author_email='arnabmitra490@gmail.com',
    author='ArnabMitra0408',
    description='sample dvc ml project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GNU',
    url='https://github.com/ArnabMitra0408/dvc-project-1',
    packages=['src'],
    python_requires='>=3.6',
    install_requires=['dvc',
                      'dvc[gdrive]',
                      'dvc[s3]',
                      'pandas',
                      'scikit-learn']

)