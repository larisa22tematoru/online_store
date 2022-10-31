import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AW2rJs5dMxlNLE8azdQoReJwgowL4bNgr7JARjoTe3nG10rwmJoGgpEdPJpCJzyzh-NTV4DiheTRAtwU"
        self.client_secret = "EO8Odo3yHDUb1YSJi7pfzkWDKeSidYccRDIjvor16ZAbjYZi8zHYSSlUgte5GutIb45aEKWpgMLmdpsV"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)