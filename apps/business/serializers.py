from rest_framework import serializers

from apps.business.models import BusinessWork, Business
from apps.config.models import ColumnTypeModel, RolesModel
from apps.tables.models import Table, Column


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    role = serializers.CharField()
    class Meta:
        model = ColumnTypeModel
        fields = ["role"]

class RoleTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ColumnTypeModel
        fields = ["name"]


class ColumnSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.CharField()
    # name = RoleTypeSerializer()
    class Meta:
        model = Column
        fields = ["id", "raw_column_name", "type"]



class TableSerializer(serializers.HyperlinkedModelSerializer):
    t_column = ColumnSerializer(many=True)

    class Meta:
        model = Table
        fields = ["id", "raw_table_name", "t_column"]

class BusinessSerializer(serializers.HyperlinkedModelSerializer):
    tables = TableSerializer(many=True)
    class Meta:
        model = Business
        fields = ["id", "name", "tables"]


class BusinessWorkSerializer(serializers.HyperlinkedModelSerializer):
    business = BusinessSerializer(many=True)

    class Meta:
        model = BusinessWork
        fields = ["id", "name", "num", "business"]
