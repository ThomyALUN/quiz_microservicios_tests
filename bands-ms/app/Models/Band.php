<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Band extends Model
{
    use HasFactory;

    protected $fillable = ['name', 'genre_id'];
    protected $hidden = ['created_at', 'updated_at'];

    public function genre()
    {
        return $this->belongsTo(Genre::class);
    }
}
