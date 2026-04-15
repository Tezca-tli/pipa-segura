import { useState } from "react";
import { Link } from "react-router-dom";
import MapView from "@/components/MapView";
import RequestForm from "@/components/RequestForm";
import { useOrders } from "@/context/OrderContext";
import { Droplets, LayoutDashboard } from "lucide-react";

const Index = () => {
  const [formOpen, setFormOpen] = useState(false);
  const { orders } = useOrders();
  const pendingCount = orders.filter((o) => o.status === "pending").length;

  return (
    <div className="h-screen w-screen flex flex-col relative overflow-hidden">
      {/* Header */}
      <header className="relative z-10 flex items-center gap-3 px-4 py-3 bg-card/80 backdrop-blur-md border-b border-border">
        <div className="flex items-center justify-center w-10 h-10 rounded-xl water-gradient">
          <Droplets className="w-5 h-5 text-primary-foreground" />
        </div>
        <div>
          <h1 className="text-lg font-bold text-foreground leading-tight">Pipa Segura</h1>
          <p className="text-xs text-muted-foreground">Ensenada, Baja California</p>
        </div>
        <div className="ml-auto flex items-center gap-3">
          <div className="flex items-center gap-1.5 text-xs text-muted-foreground">
            <span className="inline-block w-2 h-2 rounded-full bg-success" />
            5 pipas activas
          </div>
          <Link
            to="/operador"
            className="flex items-center gap-1.5 px-3 py-2 rounded-lg bg-secondary text-secondary-foreground text-xs font-medium hover:bg-secondary/80 transition-colors relative"
          >
            <LayoutDashboard className="w-3.5 h-3.5" />
            Operador
            {pendingCount > 0 && (
              <span className="absolute -top-1.5 -right-1.5 w-5 h-5 flex items-center justify-center rounded-full bg-destructive text-destructive-foreground text-[10px] font-bold">
                {pendingCount}
              </span>
            )}
          </Link>
        </div>
      </header>

      {/* Map */}
      <div className="flex-1 relative">
        <MapView />

        {/* Floating CTA */}
        <button
          onClick={() => setFormOpen(true)}
          className="absolute bottom-6 left-1/2 -translate-x-1/2 z-[1000] flex items-center gap-2.5 px-7 py-3.5 rounded-full water-gradient text-primary-foreground font-semibold text-base shadow-lg hover:shadow-xl transition-all hover:scale-105 active:scale-95"
        >
          <Droplets className="w-5 h-5" />
          Pedir Pipa
        </button>
      </div>

      <RequestForm open={formOpen} onOpenChange={setFormOpen} />
    </div>
  );
};

export default Index;
