from enum import Enum


class SampleEnum(Enum):
    FIRST_ENUM = 'first_enum'
    SECOND_ENUM = 'second_enum'


class LegalFormUS(Enum):
    INDIVIDUAL = 'individual'
    SOLE_PROPRIETOR = 'sole_proprietor'
    LIMITED_LIABILITY_COMPANY = 'limited_liability_company'
    PARTNERSHIP = 'partnership'
    CORPORATION = 'corporation'
    NONPROFIT_CORPORATION = 'nonprofit_corporation'
    UNINCORPORATED_ASSOCIATION = 'unincorporated_association'
    PERSONAL_TRUST = 'personal_trust'
    STATUTORY_TRUST = 'statutory_trust'
    GOVERNMENT_AGENCY = 'government_agency'
