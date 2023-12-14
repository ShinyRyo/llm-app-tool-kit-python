from pydantic import BaseModel, Field

class GetCryptocurrencyPriceInput(BaseModel):
    crypts: list[str] = Field(
        description="https://www.coingecko.com/apiで使用する通貨idを入力してください"
    )
    vs_currencies: str = Field(description="通貨の表現方法を入力してください")
