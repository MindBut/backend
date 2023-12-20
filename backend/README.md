<br>1. 가상 환경 세팅<br>
파이썬 버전 3.7.12 (다른 걸로 하다가 오류나서 다시 갈아엎었는데 문제가 생길 수도 있고 안 될 수도 있음)<br>
<br>
| Package                      | Version    |
|------------------------------|------------|
| absl-py                      | 2.0.0      |
| accelerate                   | 0.20.3     |
| annotated-types              | 0.5.0      |
| anyio                        | 3.7.1      |
| astunparse                   | 1.6.3      |
| bcrypt                       | 4.0.1      |
| cachetools                   | 5.3.2      |
| certifi                      | 2023.11.17 |
| cffi                         | 1.15.1     |
| charset-normalizer           | 3.3.2      |
| click                        | 8.1.7      |
| colorama                     | 0.4.6      |
| cryptography                 | 41.0.5     |
| cycler                       | 0.11.0     |
| diffusers                    | 0.21.4     |
| distro                       | 1.8.0      |
| dnspython                    | 2.3.0      |
| ecdsa                        | 0.18.0     |
| exceptiongroup               | 1.2.0      |
| fastapi                      | 0.103.2    |
| filelock                     | 3.12.2     |
| flatbuffers                  | 23.5.26    |
| flit_core                    | 3.6.0      |
| fonttools                    | 4.38.0     |
| fsspec                       | 2023.1.0   |
| gast                         | 0.4.0      |
| google-auth                  | 2.23.4     |
| google-auth-oauthlib         | 0.4.6      |
| google-pasta                 | 0.2.0      |
| greenlet                     | 2.0.1      |
| grpcio                       | 1.59.3     |
| h11                          | 0.14.0     |
| h5py                         | 3.8.0      |
| httpcore                     | 0.17.3     |
| httpx                        | 0.24.1     |
| huggingface-hub              | 0.16.4     |
| idna                         | 3.4        |
| importlib-metadata           | 6.7.0      |
| keras                        | 2.11.0     |
| kiwisolver                   | 1.4.5      |
| libclang                     | 16.0.6     |
| Markdown                     | 3.4.4      |
| MarkupSafe                   | 2.1.3      |
| matplotlib                   | 3.5.3      |
| mysql-connector              | 2.2.9      |
| mysql-connector-python       | 8.0.33     |
| numpy                        | 1.21.6     |
| oauthlib                     | 3.2.2      |
| openai                       | 1.3.5      |
| opt-einsum                   | 3.3.0      |
| packaging                    | 23.2       |
| passlib                      | 1.7.4      |
| Pillow                       | 9.5.0      |
| pip                          | 23.3.1     |
| protobuf                     | 3.19.6     |
| psutil                       | 5.9.6      |
| pyasn1                       | 0.5.1      |
| pyasn1-modules               | 0.3.0      |
| pycparser                    | 2.21       |
| pydantic                     | 2.5.2      |
| pydantic_core                | 2.14.5     |
| pymongo                      | 4.6.1      |
| PyMySQL                      | 1.1.0      |
| pyparsing                    | 3.1.1      |
| python-dateutil              | 2.8.2      |
| python-jose                  | 3.3.0      |
| python-multipart             | 0.0.6      |
| python-version               | 0.0.2      |
| PyYAML                       | 6.0.1      |
| regex                        | 2023.10.3  |
| requests                     | 2.31.0     |
| requests-oauthlib            | 1.3.1      |
| rsa                          | 4.9        |
| safetensors                  | 0.4.0      |
| scipy                        | 1.7.3      |
| setuptools                   | 68.2.2     |
| six                          | 1.16.0     |
| sniffio                      | 1.3.0      |
| SQLAlchemy                   | 1.4.39     |
| starlette                    | 0.27.0     |
| tensorboard                  | 2.11.2     |
| tensorboard-data-server      | 0.6.1      |
| tensorboard-plugin-wit       | 1.8.1      |
| tensorflow                   | 2.11.0     |
| tensorflow-estimator         | 2.11.0     |
| tensorflow-intel             | 2.11.0     |
| tensorflow-io-gcs-filesystem | 0.31.0     |
| termcolor                    | 2.3.0      |
| tokenizers                   | 0.13.3     |
| torch                        | 1.13.1     |
| torchaudio                   | 0.13.1     |
| torchvision                  | 0.14.1     |
| tqdm                         | 4.66.1     |
| transformers                 | 4.30.2     |
| typing_extensions            | 4.7.1      |
| urllib3                      | 2.0.7      |
| uvicorn                      | 0.22.0     |
| Werkzeug                     | 2.2.3      |
| wheel                        | 0.41.3     |
| wincertstore                 | 0.2        |
| wrapt                        | 1.16.0     |
| zipp                         | 3.15.0     |

<br>
2. db 세팅<br>
mysql 실행<br>
본인 비밀번호로 로그인 후<br>
create_mindbut_database.sql -> script 실행<br>
database.py에서 본인 비밀번호로 변경<br>
<br>
3. fast api 실행<br>
터미널에서 cd backend 해서 main.py가 있는 폴더까지 가야함<br>
터미널에서 uvicorn main:app --reload 하면 fastapi 실행
