<?php

namespace App\Http\Controllers;

use Http;

class BandController extends Controller
{

    protected $apiKey, $apiHeader, $baseUrl;

    public function __construct() {
        $this->apiKey = env('BANDS_API_KEY');
        $this->apiHeader = env('BANDS_API_HEADER');
        $this->baseUrl = env('BANDS_API_URL').'/bands';
    }

    public function index(){
        $response = Http::withHeaders([$this->apiHeader => $this->apiKey])
        ->get($this->baseUrl);
        return $response->json();
    }

    public function show($id){
        $response = Http::withHeaders([$this->apiHeader => $this->apiKey])
        ->get($this->baseUrl.'/'.$id);
        return $response->json();
    }
}
