class Settings:

    AUTH_TOKEN_HEADER = {'Authorization': 'Bearer keypxnt6JnEf2hYoe'}
    AUTH_TOKEN_HEADER_FOR_CREATE = {'Authorization': 'Bearer keypxnt6JnEf2hYoe', 'Content-Type': 'application/json'}
    TABLE_NAME = 'FirstTable'
    BASE_ID = 'appGFLNUsW0Et9DGN'

    LIST_RECORDS_URL = f'?maxRecords=3&view=Grid%20view'


    @property
    def get_url(self):
        return f'https://api.airtable.com/v0/{self.BASE_ID}/{self.TABLE_NAME}'
    


settings = Settings()