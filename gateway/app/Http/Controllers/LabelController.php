<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Http;

class LabelController extends Controller
{

    protected $apiKey, $apiHeader, $apiUrl;

    public function __construct() {
        $this->apiKey = env('LABELS_API_KEY');
        $this->apiHeader = env('LABELS_API_HEADER');
        $this->apiUrl = env('LABELS_API_URL');
    }

    public function generate_labels(Request $request)
    {
        $response = Http::withHeaders([$this->apiHeader => $this->apiKey])
        ->post($this->apiUrl.'/generate_labels/', $request->all());
        return $response->json();
    }

    public function get_record_labels(){
        $response = Http::withHeaders([$this->apiHeader => $this->apiKey])
        ->get($this->apiUrl.'/record_labels/');
        return $response->json();
    }
}
