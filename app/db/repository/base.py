from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, session : Session) -> None:
        self.session = session