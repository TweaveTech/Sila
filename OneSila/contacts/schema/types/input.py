from core.schema.core.types.types import auto
from core.schema.core.types.input import NodeInput, input, partial, List

from contacts.models import Company, Supplier, Customer, \
    Influencer, InternalCompany, Person, Address, \
    ShippingAddress, InvoiceAddress, InternalShippingAddress


@input(Company, fields="__all__")
class CompanyInput:
    related_companies: List['CompanyPartialInput'] | None


@partial(Company, fields="__all__")
class CompanyPartialInput(NodeInput):
    related_companies: List['CompanyPartialInput'] | None


@input(Supplier, fields="__all__")
class SupplierInput:
    pass


@partial(Supplier, fields="__all__")
class SupplierPartialInput(NodeInput):
    pass


@input(Customer, fields="__all__")
class CustomerInput:
    pass


@partial(Customer, fields="__all__")
class CustomerPartialInput(NodeInput):
    pass


@input(Influencer, fields="__all__")
class InfluencerInput:
    pass


@partial(Influencer, fields="__all__")
class InfluencerPartialInput(NodeInput):
    pass


@input(InternalCompany, fields="__all__")
class InternalCompanyInput:
    pass


@partial(InternalCompany, fields="__all__")
class InternalCompanyPartialInput(NodeInput):
    pass


@input(Person, fields="__all__")
class PersonInput:
    pass


@partial(Person, fields="__all__")
class PersonPartialInput(NodeInput):
    pass


@input(Address, fields="__all__")
class AddressInput:
    pass


@partial(Address, fields="__all__")
class AddressPartialInput(NodeInput):
    pass


@input(ShippingAddress, fields="__all__")
class ShippingAddressInput:
    pass


@partial(ShippingAddress, fields="__all__")
class ShippingAddressPartialInput(NodeInput):
    pass


@input(InvoiceAddress, fields="__all__")
class InvoiceAddressInput:
    pass


@partial(InvoiceAddress, fields="__all__")
class InvoiceAddressPartialInput(NodeInput):
    pass


@input(InternalShippingAddress, fields="__all__")
class InternalShippingAddressInput:
    pass


@partial(InternalShippingAddress, fields="__all__")
class InternalShippingAddressPartialInput(NodeInput):
    pass
