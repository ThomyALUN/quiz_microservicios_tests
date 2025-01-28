<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class GatewayFilter
{
    /**
     * Handle an incoming request.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {
        $apiKey = $request->header('BANDS-API-KEY');
        $expectedApiKey = env('API_KEY');
        if ($apiKey !== $expectedApiKey) {
            return response()->json(['message' => 'Unauthorized'], 401);
        }
        return $next($request);
    }
}
