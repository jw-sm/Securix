from pydantic import BaseModel, ConfigDict


class CoreModel(BaseModel):
    """
    Any common logic to be shared by all models goes here.
    """

    model_config = ConfigDict(from_attributes=True)


class IDModelMixin(BaseModel):
    id: int
