<?php

declare(strict_types=1);

namespace SnackAutomat\service;

class view
{
    private string $template;
    private const FILE_TYPE = 'phtml';

    public function __construct(string $template){
        $this->templates = TEMPLATE_ROOT . DIRECTORY_SEPARATOR . $templates . '.' . View::FILE_TYPE;
        if(!file_exists($this->template)){
            throw new \RuntimeException("Template not Found");
        }
    }

    public function render(?array $data=null): string{
        if($data !== null){
            extract($data);
        }

        ob_start();
        require_once $this->template;
        $content = ob_get_contents();
        ob_end_clean();

        return $content;
    }
}