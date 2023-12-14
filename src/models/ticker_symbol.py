from pydantic import BaseModel, Field


class TickerSymbol(BaseModel):
    symbol: str = Field(description="株価を知りたい企業のシンボルや通貨のシンボルを入力してください")
