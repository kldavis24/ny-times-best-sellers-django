from abc import ABC, abstractmethod


class externalService(ABC):
   
   @abstractmethod
   def external_service(self) -> str:
      return

   @abstractmethod
   def external_service_id(self) -> int:
      return