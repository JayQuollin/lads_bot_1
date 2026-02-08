
import os
from dotenv import load_dotenv
from gigachat import GigaChatAsyncClient, Chat, Messages, MessagesRole

load_dotenv()

_GIGACHAT_CLIENT = GigaChatAsyncClient(
    credentials=os.getenv("GIGA_API_KEY"), # учетные данные
    scope="GIGACHAT_API_PERS",             # область?
    model="GigaChat-2",
    ca_bundle_file="./certs/cert.pem",      # путь до файла сертификата



)


async def get_gigachat_response(user_text: str):
    payload = Chat(
        messages=[
            Messages(
                role=MessagesRole.SYSTEM,
                content="Подбери для сообщения пользователя краткую крутую пацанскую цитату, вроде 'Волк слабее льва и тигра...', и подпиши в конце ' (с) Джеймс Стетхем'.",
            ),
            Messages(role=MessagesRole.USER, content=user_text),
        ]
    )

    response = await _GIGACHAT_CLIENT.achat(payload=payload)

    return response.choices[0].message.content