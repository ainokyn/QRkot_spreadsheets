from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Кошачий благотворительный фонд'
    app_discription: str = 'Сервис для поддержки котиков!'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    type: Optional[str] = 'service_account'
    project_id: Optional[str] = 'zippy-world-354721'
    private_key_id: Optional[str] = 'de0c7b48dafa23bc188d43df9b3e9e7f32f89576'
    private_key: Optional[str] = "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC9q85yGZkWVEzo\nFhzf84zhQ0XEDyU/1+EtIkQ3fEtOkE626sS/CsySfN0V44zrtyUPmlU0ZPpUaWir\niiWeckUyKv34wJ0xPrUnRRo+UjTSCV61GTnsLcIpIrtQiVitpbA2ERvVk9SZwmU3\nXLsknjpuMjPJKIfMm9VTiGW7FZWxO/+Dxv79v5yYayCnx0N5V7+kHCUWrzFhU+OE\nOxjI+zuIAKKXsRrk6uGcEK1u2fQSV5Nh0AX8o4cm6fHur3DhwIllEdjNQJna2oAE\ny6qWBOCdu5EsthmZuchyiimQztMsSd4rKwYPuz6M1XBArAL68/20+W4H3nAlnirw\neL/G1/bVAgMBAAECggEAF7ViGOEaQbBH7LrW4SeQdJf0II3EGjbh7sJZxJXE1A01\nyaeO8FJpP+ZbvGC1PMGn4EtqWyJEKEkEzGx4R1YBUEQPewiYnY85Fa+NmDyuXZLO\nQ9TjaKJPotS0lVyVuR7858U7tXbFHHMwM7tjqTAeHago0Pw//VN9VvO1w6zvCTg/\nGp7y9JP/Ne4eajrQ1nVOmWILVCwG5msLkj0iePLne6T3kFhmLz7tNNNy5BbfOoms\nqcHkqwAdX3/vsL1Z7gg4S2d88iCX2QvEB+SpVKnKOzazPWigM1j9I4xzgTbZxJag\nunnT/aPc5NyLVIGWyHstcm0EbWdD/QaY4ZasicCAAQKBgQD9BUObN7JM2DyiZ2J5\ncql6rLxZGw8OMXPTsWFtg6u7QGh64WcPH7D/BWVoOdjcXiBOnQjXlCptNzA3q2vI\nsDJWnBlqfwkAodlVvUqsME/CE00JdZu3bjfZ1V5Ne38kbUa5VAcO8X+FURv37v8B\nK9XBa11THkDMTQjhL2/tslzupwKBgQC/55L3KdWxcMPbfZrxfH0cgdqmSeVKnFB/\n6JQFlKR80zSOC8pXiBD++KYHeLL9KPALKVK7AVLW8s9AvdtS1n0AK/orgUtJa+RB\nqjt0mxwnYmcUFjt1S7hquN8jp/zW43/6Tk+DYnzk9e32yUWnfo6M3MhkFkAYtkCa\nf4xhERK6IwKBgQDhZaUaSv2NMzyguFSjOB/+Zo7LGi3JSQiT1vqh4qBDiVcJ0G5M\nrMCyDg6OUKn9deR147KSyS0aagWMMissdroBKcICevR8GbJQjPZOeiMzEpqYCKsV\nNxyN82O0xoU24BoW0uIOz9f33Y96yO9mDbS4P3q9pr+2wBFe+TFOoIvlFQKBgF7s\nTAzH+7S+Y5LRSXADtNsB/EZerPU/5q2uPHGaOdaonglZGag8XLPSCEYP1PFWa44J\nzatEl1ZNWmjawH70K3aHSkJ0vOm/XXOBodEm3EE68mPEL3rwjnLzqSQ49t7QP0Bv\ntfL2J3MVlrSIkFSuTBKvLswbGW9fzwrc5nIpAMtjAoGAZZByNF7RSqvUBtzEjWZG\ncvxk1++FKldUxYoeA7Qcl7Zhct9opFmwSeb1oCVZLwMGHCfmm1iNT3UrP6Xvtt4p\ncYp7XwQX0VPBhx9ofCH0FSWJSi86UK6h+0YhtXtLFrvTw7FLgn0AUzsu/CiLiSHP\nbSvYINT+lyi0koVFyD8PBr0=\n-----END PRIVATE KEY-----\n"
    client_email: Optional[str] = 'aleksandra@zippy-world-354721.iam.gserviceaccount.com'
    client_id: Optional[str] = '103463856188283519816'
    auth_uri: Optional[str] = 'https://accounts.google.com/o/oauth2/auth'
    token_uri: Optional[str] = 'https://oauth2.googleapis.com/token'
    auth_provider_x509_cert_url: Optional[str] = 'https://www.googleapis.com/oauth2/v1/certs'
    client_x509_cert_url: Optional[str] = 'https://www.googleapis.com/robot/v1/metadata/x509/aleksandra%40zippy-world-354721.iam.gserviceaccount.com'
    email: Optional[str] = 'ainokyn@gmail.com'

    class Config:
        env_file = '.env'


settings = Settings()
