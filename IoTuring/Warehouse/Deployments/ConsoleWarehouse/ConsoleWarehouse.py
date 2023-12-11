from IoTuring.Logger.Logger import Logger
from IoTuring.Warehouse.Warehouse import Warehouse
from IoTuring.Entity.ValueFormat import ValueFormatter
from IoTuring.Entity.EntityData import EntitySensor
from IoTuring.Configurator.MenuPreset import MenuPreset

CONFIG_KEY_EXTRA_ATTRIBUTES = "extra"

class ConsoleWarehouse(Warehouse):
    NAME = "Console"

    def Start(self) -> None:
        self.configuredExtras = self.GetTrueOrFalseFromConfigurations(CONFIG_KEY_EXTRA_ATTRIBUTES)

        super().Start()  # Then run other inits (start the Loop method for example)


    def Loop(self) -> None:
        for entity in self.GetEntities():
            for entitySensor in entity.GetEntitySensors():
                if(entitySensor.HasValue()):
                    entityId = entitySensor.GetId()
                    self.Log(Logger.LOG_MESSAGE, entityId +
                             ": " + self.FormatValue(entitySensor))
                    if entitySensor.HasExtraAttributes() and self.configuredExtras:
                        for attribute in entitySensor.extraAttributes:
                            self.Log(Logger.LOG_MESSAGE, 
                                     f"{entityId}: {attribute.GetName()}:{attribute.GetValue()}")

    def FormatValue(self, entitySensor: EntitySensor):
        return ValueFormatter.FormatValue(entitySensor.GetValue(), entitySensor.GetValueFormatterOptions(), True)
    
    @classmethod
    def ConfigurationPreset(cls) -> MenuPreset:
        preset = MenuPreset()
        preset.AddEntry("Should ExtraAttributes be displayed in Console",
                        CONFIG_KEY_EXTRA_ATTRIBUTES, 
                        mandatory=False,
                        question_type="yesno")
        return preset