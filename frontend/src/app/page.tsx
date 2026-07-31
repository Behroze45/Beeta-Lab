"use client";

import { useHealth } from "@/lib/hooks/use-health";

export default function HomePage() {
  const { data, isLoading, isError } = useHealth();

  return (
    <main className="flex min-h-screen items-center justify-center p-8">
      <div className="space-y-4 text-center">
        <h1 className="text-4xl font-bold">Beeta Lab</h1>

        <p className="text-gray-500">
          AI-powered Historical Intelligence Platform
        </p>

        {isLoading && <p>Checking backend...</p>}

        {isError && (
          <p className="text-red-500">
            Backend is not available yet.
          </p>
        )}

        {data && (
          <p className="text-green-600">
            Backend Status: {data.status}
          </p>
        )}
      </div>
    </main>
  );}