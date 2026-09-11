from datetime import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict, Field, model_validator


# --- Category Schemas ---
class FgCategoryBase(BaseModel):
    id: str
    name: str

    model_config = ConfigDict(populate_by_name=True, from_attributes=True)


class FgCategoryCreate(BaseModel):
    id: str | None = None
    name: str
    created_by: str | None = Field(default="admin", alias="createdBy")

    model_config = ConfigDict(populate_by_name=True)


class FgCategoryResponse(FgCategoryBase):
    created_on: datetime = Field(..., alias="createdOn")
    created_by: str | None = Field(None, alias="createdBy")
    updated_on: datetime | None = Field(None, alias="updatedOn")
    updated_by: str | None = Field(None, alias="updatedBy")


# --- Status Schemas ---
class FgStatusBase(BaseModel):
    id: str
    name: str

    model_config = ConfigDict(populate_by_name=True, from_attributes=True)


class FgStatusCreate(BaseModel):
    id: str | None = None
    name: str
    created_by: str | None = Field(default="admin", alias="createdBy")

    model_config = ConfigDict(populate_by_name=True)


class FgStatusResponse(FgStatusBase):
    created_on: datetime = Field(..., alias="createdOn")
    created_by: str | None = Field(None, alias="createdBy")
    updated_on: datetime | None = Field(None, alias="updatedOn")
    updated_by: str | None = Field(None, alias="updatedBy")


# --- Dimensions Helper Schema ---
class DimensionsSchema(BaseModel):
    length_mm: int | None = Field(None, alias="lengthMm")
    width_mm: int | None = Field(None, alias="widthMm")
    height_mm: int | None = Field(None, alias="heightMm")

    model_config = ConfigDict(populate_by_name=True, from_attributes=True)


# --- Master Data Item Schemas ---
class MasterDataItemCreate(BaseModel):
    id: str | None = None
    fg_image: str | None = Field(None, alias="fgImage")
    material_code: str = Field(..., alias="materialCode")
    part_number: str = Field(..., alias="partNumber")
    category_id: str | None = Field(None, alias="categoryId")
    category: str | None = None  # Accepts category name (e.g. "Mattress") or ID
    model: str | None = None
    product_description: str | None = Field(None, alias="productDescription")
    dimensions: DimensionsSchema | None = None
    length_mm: int | None = Field(None, alias="lengthMm")
    width_mm: int | None = Field(None, alias="widthMm")
    height_mm: int | None = Field(None, alias="heightMm")
    net_weight: float | None = Field(None, alias="netWeight")
    gross_weight: float | None = Field(None, alias="grossWeight")
    package_type: str | None = Field(None, alias="packageType")
    status_id: str | None = Field(None, alias="statusId")
    status: str | None = None  # Accepts status name (e.g. "Active") or ID
    created_by: str | None = Field(default="admin", alias="createdBy")

    model_config = ConfigDict(populate_by_name=True)


class MasterDataItemUpdate(BaseModel):
    fg_image: str | None = Field(None, alias="fgImage")
    material_code: str | None = Field(None, alias="materialCode")
    part_number: str | None = Field(None, alias="partNumber")
    category_id: str | None = Field(None, alias="categoryId")
    category: str | None = None
    model: str | None = None
    product_description: str | None = Field(None, alias="productDescription")
    dimensions: DimensionsSchema | None = None
    length_mm: int | None = Field(None, alias="lengthMm")
    width_mm: int | None = Field(None, alias="widthMm")
    height_mm: int | None = Field(None, alias="heightMm")
    net_weight: float | None = Field(None, alias="netWeight")
    gross_weight: float | None = Field(None, alias="grossWeight")
    package_type: str | None = Field(None, alias="packageType")
    status_id: str | None = Field(None, alias="statusId")
    status: str | None = None
    updated_by: str | None = Field(default="admin", alias="updatedBy")

    model_config = ConfigDict(populate_by_name=True)


class MasterDataItemResponse(BaseModel):
    id: str
    fg_image: str | None = Field(None, alias="fgImage")
    material_code: str = Field(..., alias="materialCode")
    part_number: str = Field(..., alias="partNumber")
    category_id: str = Field(..., alias="categoryId")
    category: str | None = None
    model: str | None = None
    product_description: str | None = Field(None, alias="productDescription")
    product_name: str | None = Field(None, alias="productName")
    dimensions: DimensionsSchema
    net_weight: float | None = Field(None, alias="netWeight")
    gross_weight: float | None = Field(None, alias="grossWeight")
    package_type: str | None = Field(None, alias="packageType")
    status_id: str = Field(..., alias="statusId")
    status: str | None = None
    created_on: datetime = Field(..., alias="createdOn")
    created_by: str | None = Field(None, alias="createdBy")
    updated_on: datetime | None = Field(None, alias="updatedOn")
    updated_by: str | None = Field(None, alias="updatedBy")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )

    @model_validator(mode="before")
    @classmethod
    def transform_orm_and_payload(cls, data: Any) -> Any:
        if hasattr(data, "__table__"):
            # Reading from SQLAlchemy ORM instance
            category_rel = getattr(data, "category", None)
            status_rel = getattr(data, "status", None)
            category_name = category_rel.name if category_rel else getattr(data, "category_id", None)
            status_name = status_rel.name if status_rel else getattr(data, "status_id", None)

            dimensions_dict = {
                "lengthMm": getattr(data, "length_mm", None),
                "widthMm": getattr(data, "width_mm", None),
                "heightMm": getattr(data, "height_mm", None),
            }

            prod_name = getattr(data, "model", None) or getattr(data, "product_description", None)

            net_wt = getattr(data, "net_weight", None)
            if net_wt is not None:
                net_wt = float(net_wt)

            gross_wt = getattr(data, "gross_weight", None)
            if gross_wt is not None:
                gross_wt = float(gross_wt)

            return {
                "id": data.id,
                "fg_image": data.fg_image,
                "material_code": data.material_code,
                "part_number": data.part_number,
                "category_id": data.category_id,
                "category": category_name,
                "model": data.model,
                "product_description": data.product_description,
                "product_name": prod_name,
                "dimensions": dimensions_dict,
                "net_weight": net_wt,
                "gross_weight": gross_wt,
                "package_type": data.package_type,
                "status_id": data.status_id,
                "status": status_name,
                "created_on": data.created_on,
                "created_by": data.created_by,
                "updated_on": data.updated_on,
                "updated_by": data.updated_by,
            }
        return data


class MasterDataListResponse(BaseModel):
    success: bool = True
    count: int
    data: list[MasterDataItemResponse]

    model_config = ConfigDict(populate_by_name=True)

