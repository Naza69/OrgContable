#include <iostream>
#include <string>
#include <unordered_map>

class CarInsurance {
public:
    struct Policy {
        std::string carOwner;
        std::string carModel;
        float premium;
        bool isActive;

        Policy(const std::string& owner, const std::string& model, float premium)
            : carOwner(owner), carModel(model), premium(premium), isActive(true) {}
    };

    void registerCar(const std::string& plate, const std::string& owner, const std::string& model, float premium) {
        if (policies.find(plate) != policies.end()) {
            std::cout << "Error: El coche ya está registrado." << std::endl;
            return;
        }
        policies[plate] = Policy(owner, model, premium);
        std::cout << "Coche registrado: " << plate << " para el propietario " << owner << "." << std::endl;
    }

    void activatePolicy(const std::string& plate) {
        if (policies.find(plate) == policies.end()) {
            std::cout << "Error: Coche no registrado." << std::endl;
            return;
        }
        policies[plate].isActive = true;
        std::cout << "Póliza activada para el coche: " << plate << "." << std::endl;
    }

    void deactivatePolicy(const std::string& plate) {
        if (policies.find(plate) == policies.end()) {
            std::cout << "Error: Coche no registrado." << std::endl;
            return;
        }
        policies[plate].isActive = false;
        std::cout << "Póliza desactivada para el coche: " << plate << "." << std::endl;
    }

    void checkPolicy(const std::string& plate) {
        if (policies.find(plate) == policies.end()) {
            std::cout << "Error: Coche no registrado." << std::endl;
            return;
        }
        const Policy& policy = policies[plate];
        std::cout << "Coche: " << plate << "\n"
                  << "Propietario: " << policy.carOwner << "\n"
                  << "Modelo: " << policy.carModel << "\n"
                  << "Prima: " << policy.premium << "\n"
                  << "Estado: " << (policy.isActive ? "Activo" : "Inactivo") << std::endl;
    }

private:
    std::unordered_map<std::string, Policy> policies;
};

int main() {
    CarInsurance insurance;

    insurance.registerCar("ABC123", "Sergio Neira", "Tesla Model Y", 500.0);
    insurance.checkPolicy("ABC123");

    insurance.activatePolicy("ABC123");
    insurance.checkPolicy("ABC123");

    insurance.deactivatePolicy("ABC123");
    insurance.checkPolicy("ABC123");

    return 0;
}
