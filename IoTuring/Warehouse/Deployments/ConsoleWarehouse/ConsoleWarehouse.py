from IoTuring.Logger.Logger import Logger
from IoTuring.Warehouse.Warehouse import Warehouse
from IoTuring.Entity.ValueFormat import ValueFormatter
from IoTuring.Entity.EntityData import EntitySensor

class ConsoleWarehouse(Warehouse):
    NAME = "Console"

    def Loop(self):
        for entity in self.GetEntities():
            for entitySensor in entity.GetEntitySensors():
                if(entitySensor.HasValue()):
                    entityId = entitySensor.GetId
                    self.Log(Logger.LOG_MESSAGE, entityId +
                             ": " + self.FormatValue(entitySensor))
                    if entitySensor.HasExtraAttributes():
                        for attribute in entitySensor.extraAttributes:
                            self.Log(Logger.LOG_MESSAGE, 
                                     f"{entityId}: {attribute.GetName()}:{attribute.GetValue()}")

    def FormatValue(self, entitySensor: EntitySensor):
        return ValueFormatter.FormatValue(entitySensor.GetValue(), entitySensor.GetValueFormatterOptions(), True)